import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03467, -0.04525).lineTo(-0.05506, -0.05078).lineTo(-0.05506, -0.05871).lineTo(0.04775, -0.05757).lineTo(0.04775, -0.05104).lineTo(0.02015, -0.0445).lineTo(-0.03467, -0.04525).close()
solid=wp_sketch0.add(loop0).extrude(-0.25515112766106035)
