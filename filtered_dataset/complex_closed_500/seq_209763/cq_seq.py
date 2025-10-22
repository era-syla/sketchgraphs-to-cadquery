import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04132, 0.04).threePointArc((-0.043, 0.01998), (-0.04094, -0.0)).lineTo(-0.037, 0.0).lineTo(-0.037, 0.04).lineTo(-0.04132, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.042856721849125215)
