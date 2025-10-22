import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.02337).lineTo(0.05839, -0.02337).lineTo(0.05839, -0.03202).lineTo(-0.0, -0.02337).close()
solid=wp_sketch0.add(loop0).extrude(-0.017406818799325173)
