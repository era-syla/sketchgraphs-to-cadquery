import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0).lineTo(-0.0614, 0.03933).lineTo(-0.04237, 0.08494).lineTo(0.03597, 0.06737).lineTo(0.03457, 0.03709).lineTo(0.00239, 0.03293).lineTo(-0.0054, 0.05783).lineTo(0.02216, 0.07209).lineTo(0.04221, 0.04583).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.042773972985678164)
