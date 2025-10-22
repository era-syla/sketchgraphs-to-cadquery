import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.80035, 2.7178).lineTo(-2.63525, 2.7178).lineTo(-2.63525, 2.4384).lineTo(-2.80035, 2.4384).lineTo(-2.80035, 2.7178).close()
solid=wp_sketch0.add(loop0).extrude(0.6284008592629103)
