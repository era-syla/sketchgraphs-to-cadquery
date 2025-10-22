import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03474, -0.16548).lineTo(0.05974, -0.16548).lineTo(0.05974, -0.27548).lineTo(0.03474, -0.27548).lineTo(0.03474, -0.16548).close()
solid=wp_sketch0.add(loop0).extrude(0.03266667718526336)
