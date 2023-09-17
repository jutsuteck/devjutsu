import { NextPage } from "next";

import CenteredContainer from "@/components/layout/CenteredContainer";
import { useVerifyUser } from "@/hooks/auth/useVerifyUser";
import { useRouter } from "next/router";
import Card from "@/components/ui/Card";

const VerifyPage: NextPage = () => {
  const router = useRouter();
  const { token } = router.query;
  const { isVerified, message } = useVerifyUser(token as string);

  return (
    <CenteredContainer>
      <Card>
        <h1 className="text-4xl font-extrabold mb-4">
          Verification Successful!
        </h1>
        <p>
          Thank you for verifying your email address. Your account is now
          active.
        </p>
        <p
          className="underline mt-6 cursor-pointer"
          onClick={() => router.push("/login")}
        >
          Login here
        </p>
      </Card>
    </CenteredContainer>
  );
};

export default VerifyPage;
