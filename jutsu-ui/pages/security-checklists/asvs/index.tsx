import { NextPage } from "next";

import AsvsList from "@/components/ui/AsvsList";
import TopBar from "@/components/ui/TopBar";

const AsvsPage: NextPage = () => {
  return (
    <>
      <TopBar />
      <div className="px-8">
        <h1 className="text-sm text-nord-polar-night-light my-4">
          Security Checklists /{" "}
          <span className="font-semibold">
            Application Security Verification Standard (ASVS)
          </span>
        </h1>
        <AsvsList />
      </div>
    </>
  );
};

export default AsvsPage;
