import { NextPage } from "next";
import { useState } from "react";

import Container from "@/components/layout/Container";
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
    <Container flexCol centered>
      <Card transparent>
        <h1 className="text-5xl font-extrabold text-nord-snowstorm-light mb-6 text-center">
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
    </Container>
  );
};

export default LoginPage;
