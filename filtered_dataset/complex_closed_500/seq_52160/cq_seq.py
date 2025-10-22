import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0286, 0.03333).lineTo(0.0294, 0.03333).lineTo(0.0294, -0.02967).lineTo(-0.0286, -0.02967).lineTo(-0.0286, 0.03333).close()
solid=wp_sketch0.add(loop0).extrude(-0.043992394754487685)
