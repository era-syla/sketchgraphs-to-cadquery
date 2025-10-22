import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00541, 0.0132).threePointArc((-0.00724, 0.00856), (-0.00907, 0.0132)).lineTo(-0.00907, 0.00928).threePointArc((-0.00724, 0.00856), (-0.00541, 0.00928)).lineTo(-0.00541, 0.0132).close()
solid=wp_sketch0.add(loop0).extrude(0.006972619748011159)
