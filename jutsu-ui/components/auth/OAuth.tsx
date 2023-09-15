import { FC } from "react";
import { AiFillGithub } from "react-icons/ai";

import Button from "../ui/Button";

const OAuth: FC = () => {
  return (
    <>
      <Button icon={<AiFillGithub />} text="Continue with Github" transparent />
    </>
  );
};

export default OAuth;
