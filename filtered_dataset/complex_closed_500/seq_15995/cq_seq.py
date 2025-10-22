import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.71093, 0.5104).lineTo(0.08907, 0.5104).lineTo(0.08907, 0.0104).threePointArc((0.0012, -0.20173), (-0.21093, -0.2896)).lineTo(-1.71093, -0.2896).lineTo(-1.71093, 0.5104).close()
solid=wp_sketch0.add(loop0).extrude(1.0253751274879899)
