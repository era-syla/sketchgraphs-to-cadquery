import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01775, 0.0317).lineTo(-0.01525, 0.0317).lineTo(-0.01525, 0.0342).lineTo(-0.01775, 0.0342).lineTo(-0.01775, 0.0317).close()
solid=wp_sketch0.add(loop0).extrude(-0.0012868806221115092)
