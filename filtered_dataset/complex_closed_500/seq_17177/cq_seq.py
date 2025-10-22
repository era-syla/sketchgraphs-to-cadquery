import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.38076, 0.07903).threePointArc((-0.40499, -0.04277), (-0.30174, -0.11176)).lineTo(0.96826, -0.11176).lineTo(0.96826, -0.0635).lineTo(-0.30174, -0.0635).threePointArc((-0.3604, -0.0243), (-0.34664, 0.0449)).lineTo(0.10237, 0.49391).lineTo(0.06825, 0.52804).lineTo(-0.38076, 0.07903).close()
solid=wp_sketch0.add(loop0).extrude(1.4969674331437983)
