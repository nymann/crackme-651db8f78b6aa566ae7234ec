"""
int keyHasFourSegmentsSeparatedByHyphens(char *key)

{
  int iVar1;
  size_t key_length;
  int local_c;

  key_length = strlen(key);
  if (key_length == (long)(segment_count + segment_count * segment_length + -1)) {
    for (local_c = 0; local_c < segment_count + -1; local_c = local_c + 1) {
      if (key[segment_length + (segment_length + 1) * local_c] != '-') {
        return 0;
      }
    }
    iVar1 = 1;
  }
  else {
    iVar1 = 0;
  }
  return iVar1;
}
"""


def key_segment_checker(key: str, segment_count: int, segment_length: int) -> bool:
    segments = key.split("-")
    if len(segments) != segment_count:
        return False
    for segment in segments:
        if len(segment) != segment_length:
            return False
    return True


def key_format_is_valid(key: str) -> bool:
    return key_segment_checker(key=key, segment_count=4, segment_length=4) and len(key) == 19


"""
int isKeyValid(char *key)

{
  int segment_is_valid;
  int previous_segment_sum;
  int segment_index;
  int segment_sum;
  int i;

  previous_segment_sum = 0;
  segment_index = 0;
  while( true ) {
    if (segment_count <= segment_index) {
      return 1;
    }
    segment_sum = 0;
    for (i = 0; i < segment_length; i = i + 1) {
      segment_sum = segment_sum + key[i + segment_index * 5];
    }
    segment_is_valid = isSegmentValid(segment_sum);
    if ((char)segment_is_valid != '\x01') break;
    if (segment_sum <= previous_segment_sum) {
      return 0;
    }
    previous_segment_sum = segment_sum;
    segment_index = segment_index + 1;
  }
  return 0;
}
"""


def key_is_valid(key: str) -> bool:
    segments = key.split("-")
    previous_segment_sum = 0
    for segment in segments:
        segment_sum = sum(ord(c) for c in segment)
        if segment_sum <= previous_segment_sum:
            return False
        if not segment_is_valid(segment):
            return False
        previous_segment_sum = segment_sum
    return True


"""
int isSegmentValid(int segment_sum)

{
  int result;
  int i;

  if ((segment_sum == 0) || (segment_sum == 1)) {
    result = 0;
  }
  else {
    for (i = 2; i < segment_sum / 2; i = i + 1) {
      if (segment_sum % i == 0) {
        return 0;
      }
    }
    result = 1;
  }
  return result;
}
"""


def segment_is_valid(segment: str) -> bool:
    segment_sum = sum(ord(c) for c in segment)
    if segment_sum < 2:
        return False
    for i in range(2, (int)(segment_sum / 2)):
        if segment_sum % i == 0:
            return False
    return True


def crackme(key: str) -> bool:
    return key_format_is_valid(key) and key_is_valid(key)
