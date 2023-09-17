import { GetServerSideProps, NextPage } from "next";
import { useEffect } from "react";

import Cookies from "js-cookie";
import CenteredContainer from "@/components/layout/CenteredContainer";
import Card from "@/components/ui/Card";

const SignUpSuccessPage: NextPage = () => {
  const email = Cookies.get("registeredEmail") || "";

  useEffect(() => {
    Cookies.remove("userRegistered");
    Cookies.remove("registeredEmail");
  }, []);

  return (
    <CenteredContainer>
      <Card>
        <h1 className="text-4xl font-extrabold mb-4">
          Registration successful!
        </h1>
        <p>
          Thank you for registering. A verification link has been sent to{" "}
          <span className="underline">{email}</span>
        </p>
      </Card>
    </CenteredContainer>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
  const isRegistered = context.req.cookies.userRegistered;

  if (!isRegistered) {
    return {
      redirect: {
        destination: "/signup",
        permanent: false,
      },
    };
  }

  return {
    props: {},
  };
};

export default SignUpSuccessPage;
