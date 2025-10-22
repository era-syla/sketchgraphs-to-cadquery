import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.84, 0.56).lineTo(-0.84, 0.56).lineTo(-0.84, -0.56).lineTo(0.84, -0.56).lineTo(0.84, 0.56).close()
solid=wp_sketch0.add(loop0).extrude(4.867564415538171)
