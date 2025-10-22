import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.9801, -0.28515).lineTo(-0.53179, -0.28515).lineTo(-0.53179, -0.80966).lineTo(-0.9801, -0.80966).lineTo(-0.9801, -0.28515).close()
solid=wp_sketch0.add(loop0).extrude(-0.47480048707521116)
