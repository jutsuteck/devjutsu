import { FC, useState } from "react";
import { motion } from "framer-motion";

import useAsvs from "@/hooks/projects/useAsvs";

import Masonry from "../layout/Masonry";
import Card from "./Card";
import CustomDropdown from "./CustomDropdown";

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

  const categoryOptions =
    asvsCategories?.map((category) => category.name) || [];
  const subCategoryOptions = selectedCategory
    ? asvsCategories
        ?.find((category) => category.name === selectedCategory)
        ?.sub_categories.map((sub) => sub.name) || []
    : [];

  if (isLoading) {
    return <p>Is loading ...</p>;
  }

  const asvsRequirements =
    asvsCategories?.flatMap((category) =>
      category.sub_categories.flatMap((subCategory) =>
        subCategory.security_requirements.map((requirement) => ({
          ...requirement,
          categoryName: category.name,
          subCategoryName: subCategory.name,
        }))
      )
    ) || [];

  const filteredRequirements = asvsRequirements.filter(
    (req) =>
      (!selectedCategory || req.categoryName === selectedCategory) &&
      (!selectedSubCategory || req.subCategoryName === selectedSubCategory)
  );

  return (
    <>
      <div className="space-x-4">
        <CustomDropdown
          options={categoryOptions}
          onSelect={setSelectedCategory}
          label="Select Category"
        />
        {selectedCategory && (
          <CustomDropdown
            options={subCategoryOptions}
            onSelect={setSelectedSubCategory}
            label="Select SubCategory"
          />
        )}
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
                <p>{requirement.description}</p>
              </Card>
            </motion.div>
          ))}
        </Masonry>
      </div>
    </>
  );
};

export default AsvsList;
