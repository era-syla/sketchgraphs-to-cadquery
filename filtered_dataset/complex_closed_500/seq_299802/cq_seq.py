import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0702, 0.66987).lineTo(0.0698, 0.66987).lineTo(0.0698, -0.15013).lineTo(-0.0702, -0.15013).lineTo(-0.0702, 0.66987).close()
solid=wp_sketch0.add(loop0).extrude(-1.2691371238810332)
