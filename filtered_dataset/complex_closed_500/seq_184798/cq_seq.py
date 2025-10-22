import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.41992, -0.23691).lineTo(0.50313, -0.36401).lineTo(0.48974, -0.37277).lineTo(0.4008, -0.23691).lineTo(0.41992, -0.23691).close()
solid=wp_sketch0.add(loop0).extrude(-0.14228863959133042)
