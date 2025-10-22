import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03355, 0.05517).threePointArc((-0.08629, 0.0617), (-0.13931, 0.0652)).lineTo(-0.12899, 0.1219).lineTo(0.07392, 0.08496).lineTo(0.05592, -0.06891).lineTo(-0.13931, -0.10155).lineTo(-0.2, -0.06328).threePointArc((-0.13074, -0.05962), (-0.06169, -0.0531)).threePointArc((-0.01766, -0.03025), (-0.0, 0.0161)).threePointArc((-0.00954, 0.04185), (-0.03355, 0.05517)).close()
solid=wp_sketch0.add(loop0).extrude(0.08337017233010913)
