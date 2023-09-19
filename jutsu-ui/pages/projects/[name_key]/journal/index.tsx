import Dashboard from "@/components/layout/Dashboard";
import { NextPage } from "next";
import { useRouter } from "next/router";

const JournalPage: NextPage = () => {
  const router = useRouter();
  const { projectId } = router.query;
  return (
    <Dashboard projectId={projectId} pageName="Journal">
      <h1></h1>
    </Dashboard>
  );
};

export default JournalPage;
