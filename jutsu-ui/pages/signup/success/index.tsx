import { GetServerSideProps, NextPage } from "next";
import { useEffect } from "react";

import Cookies from "js-cookie";
import CenteredContainer from "@/components/layout/CenteredContainer";

const SignUpSuccessPage: NextPage = () => {
  // useEffect(() => {
  //   Cookies.remove("userRegistered");
  // }, []);

  return (
    <CenteredContainer>
      <h1>Registration successfull</h1>
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
