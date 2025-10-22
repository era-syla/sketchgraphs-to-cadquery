import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0116, 0.0076).lineTo(0.0116, 0.0076).lineTo(0.0116, -0.0076).lineTo(-0.0116, -0.0076).lineTo(-0.0116, 0.0076).close()
solid=wp_sketch0.add(loop0).extrude(-0.008378274155846792)
