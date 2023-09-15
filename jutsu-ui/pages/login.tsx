import { NextPage } from "next";
import { useState } from "react";

import CenteredContainer from "@/components/layout/CenteredContainer";
import Card from "@/components/ui/Card";
import OAuth from "@/components/auth/OAuth";
import ForgotPasswordForm from "@/components/auth/ForgotPasswordForm";
import LoginForm from "@/components/auth/LoginForm";

const LoginPage: NextPage = () => {
  const [forgotPassword, setForgotPassword] = useState(false);

  const onClickHandleForgotPassword = () => {
    setForgotPassword(!forgotPassword);
  };

  return (
    <CenteredContainer flexCol>
      <Card transparent>
        <h1 className="text-5xl text-nord-snowstorm-light mb-6 text-center">
          Login
        </h1>

        <OAuth />

        <hr className="my-6 border-t border-nord-polar-night-light" />

        {forgotPassword ? <ForgotPasswordForm /> : <LoginForm />}

        <p
          className="text-center underline mt-6 cursor-pointer"
          onClick={onClickHandleForgotPassword}
        >
          {forgotPassword ? "Back to login" : "Forgot password?"}
        </p>
      </Card>
    </CenteredContainer>
  );
};

export default LoginPage;
