import { FC, useState } from "react";
import { motion } from "framer-motion";

import useAsvs from "@/hooks/projects/useAsvs";

import Masonry from "../layout/Masonry";
import Card from "./Card";
import Button from "./Button";

import { MdOutlineCancel } from "react-icons/md";

const fadeIn = {
  hidden: { opacity: 0 },
  visible: (i: number) => ({
    opacity: 1,
    transition: { delay: Math.random(), duration: 0.5 },
  }),
};

const AsvsList: FC = () => {
  const { data: asvsCategories, isLoading, isError } = useAsvs();
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [selectedSubCategory, setSelectedSubCategory] = useState<string | null>(
    null
  );

  if (isLoading) {
    return <p>Is loading ...</p>;
  }

  const handleCategoryClick = (categoryName: string) => {
    if (selectedCategory === categoryName) {
      setSelectedCategory(null);
      setSelectedSubCategory(null);
    } else {
      setSelectedCategory(categoryName);
      setSelectedSubCategory(null);
    }
  };

  const handleSubCategoryClick = (subCategoryName: string) => {
    if (selectedSubCategory === subCategoryName) {
      setSelectedSubCategory(null);
    } else {
      setSelectedSubCategory(subCategoryName);
    }
  };

  const filteredRequirements =
    asvsCategories
      ?.flatMap((category) =>
        category.sub_categories.flatMap((subCategory) =>
          subCategory.security_requirements.map((requirement) => ({
            ...requirement,
            categoryName: category.name,
            subCategoryName: subCategory.name,
          }))
        )
      )
      .filter(
        (req) =>
          (!selectedCategory || req.categoryName === selectedCategory) &&
          (!selectedSubCategory || req.subCategoryName === selectedSubCategory)
      ) || [];

  return (
    <>
      <div className="flex space-x-4 mb-4">
        {selectedCategory ? (
          <Button
            icon={<MdOutlineCancel />}
            text={selectedCategory}
            shadow="shadow-md"
            polarNightMedium
            onClick={() => handleCategoryClick(selectedCategory)}
          />
        ) : (
          asvsCategories?.map((category) => (
            <Button
              key={category.id}
              onClick={() => handleCategoryClick(category.name)}
              text={category.name}
              bgPolarNightDarkest
              shadow="shadow-md"
            />
          ))
        )}

        {selectedCategory &&
          asvsCategories
            ?.find((category) => category.name === selectedCategory)
            ?.sub_categories.map((subCategory) => (
              <Button
                key={subCategory.id}
                onClick={() => handleSubCategoryClick(subCategory.name)}
                text={subCategory.name}
                bgPolarNightDarkest
                shadow="shadow-md"
              />
            ))}
      </div>

      <div className="mb-4 flex space-x-4">
        <Masonry gap={{ horizontal: 15, vertical: 15 }}>
          {filteredRequirements?.map((requirement, i) => (
            <motion.div
              key={requirement.id}
              initial="hidden"
              animate="visible"
              variants={fadeIn}
              custom={i}
            >
              <Card className="hover:cursor-pointer" boxShadow="shadow-lg">
                <span className="py-1 px-2 rounded-full bg-nord-frost-light text-nord-frost-dark text-sm font-semibold">
                  {requirement.requirement_id}
                </span>
                <h1 className="my-1 text-lg font-extrabold">
                  {requirement.categoryName}
                </h1>
                <h2 className="mb-2 font-bold text-nord-polar-night-light">
                  {requirement.subCategoryName}
                </h2>
                <p className="mb-2">{requirement.description}</p>
                <p className="text-sm">{requirement.levels}</p>
              </Card>
            </motion.div>
          ))}
        </Masonry>
      </div>
    </>
  );
};

export default AsvsList;
