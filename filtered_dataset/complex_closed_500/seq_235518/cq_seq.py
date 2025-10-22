import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04445, 0.5334).lineTo(-0.03335, 0.5334).lineTo(-0.03122, 0.53086).lineTo(-0.04699, 0.53086).lineTo(-0.04699, 0.5427).lineTo(-0.03071, 0.5427).lineTo(-0.03241, 0.53975).lineTo(-0.04445, 0.53975).lineTo(-0.04445, 0.5334).close()
solid=wp_sketch0.add(loop0).extrude(-0.04568913224788742)
