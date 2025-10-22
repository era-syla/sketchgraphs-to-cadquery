import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06209, 0.00572).lineTo(-0.01095, 0.01501).lineTo(0.00804, 0.02276).lineTo(0.03226, 0.02276).lineTo(0.05124, 0.0154).lineTo(0.05841, 0.00746).lineTo(0.05841, 0.0).lineTo(-0.02567, 0.0).lineTo(-0.07623, 0.0).lineTo(-0.06209, 0.00572).close()
solid=wp_sketch0.add(loop0).extrude(0.25223128234702247)
