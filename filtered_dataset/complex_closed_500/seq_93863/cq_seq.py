import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.01969).lineTo(-0.00317, -0.01969).threePointArc((-0.00406, -0.0188), (-0.00318, -0.01791)).lineTo(-0.0, -0.01791).lineTo(0.0, -0.01969).close()
solid=wp_sketch0.add(loop0).extrude(0.0025095180164181555)
