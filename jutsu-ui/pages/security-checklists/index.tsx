import Card from "@/components/ui/Card";
import TopBar from "@/components/ui/TopBar";
import { NextPage } from "next";
import { useRouter } from "next/router";

const SecurityChecklists: NextPage = () => {
  const router = useRouter();

  return (
    <>
      <TopBar />
      <div className="p-4">
        <Card
          maxSize="fit"
          className="hover:cursor-pointer"
          onClick={() => router.push("/security-checklists/asvs")}
        >
          <h1 className="text-xl font-bold">ASVS</h1>
        </Card>
      </div>
    </>
  );
};

export default SecurityChecklists;
