import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.20408, -0.0008).lineTo(-0.2295, 0.00254).lineTo(-0.2295, -0.0055).lineTo(-0.20809, -0.0055).threePointArc((-0.2055, -0.00801), (-0.20308, -0.00533)).lineTo(-0.20408, -0.0008).close()
solid=wp_sketch0.add(loop0).extrude(0.01888875664061523)
