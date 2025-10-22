import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0025, 0.07389).lineTo(0.002, 0.07389).lineTo(0.002, -0.00254).lineTo(-0.0025, -0.00254).lineTo(-0.0025, 0.07389).close()
solid=wp_sketch0.add(loop0).extrude(0.12174225225793035)
