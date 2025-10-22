import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04445, 0.01905).lineTo(-0.04445, 0.01905).lineTo(-0.04445, -0.01905).lineTo(0.04445, -0.01905).lineTo(0.04445, 0.01905).close()
solid=wp_sketch0.add(loop0).extrude(-0.11620579190383629)
