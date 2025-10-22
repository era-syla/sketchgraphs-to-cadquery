import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04826, -0.0127).lineTo(0.04826, 0.0127).lineTo(-0.04826, 0.0127).lineTo(-0.04826, -0.0127).lineTo(-0.02667, -0.0127).lineTo(-0.02667, -0.03302).lineTo(0.02667, -0.03302).lineTo(0.02667, -0.0127).lineTo(0.04826, -0.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.04588261707545835)
