import { useEffect } from "react";

const useHideForm = (isVisible: boolean, hideFunction: () => void) => {
  useEffect(() => {
    const handleEscapePress = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        hideFunction();
      }
    };

    const handleFocusOut = (event: FocusEvent) => {
      if (!event.currentTarget.contains(event.relatedTarget as Node)) {
        hideFunction();
      }
    };

    if (isVisible) {
      document.addEventListener("keydown", handleEscapePress);
      document.addEventListener("focusout", handleFocusOut);
    }

    return () => {
      document.removeEventListener("keydown", handleEscapePress);
      document.removeEventListener("focusout", handleFocusOut);
    };
  }, [isVisible, hideFunction]);
};

export default useHideForm;
