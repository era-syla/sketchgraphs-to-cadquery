import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.082).lineTo(0.0, 0.057).lineTo(-0.005, 0.057).lineTo(-0.005, -0.057).lineTo(0.0, -0.057).lineTo(0.0, -0.082).lineTo(-0.001, -0.082).lineTo(-0.001, -0.058).lineTo(-0.006, -0.058).lineTo(-0.006, 0.058).lineTo(-0.001, 0.058).lineTo(-0.001, 0.082).lineTo(0.0, 0.082).close()
solid=wp_sketch0.add(loop0).extrude(-0.006830141139108719)
