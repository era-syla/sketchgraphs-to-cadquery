import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01787, 0.00696).lineTo(0.0117, 0.00696).threePointArc((0.0096, 0.00761), (0.0074, 0.00771)).lineTo(0.0074, 0.006).lineTo(0.0088, 0.006).lineTo(0.0218, 0.006).lineTo(0.0218, 0.0065).lineTo(0.01787, 0.00723).lineTo(0.01787, 0.00696).close()
solid=wp_sketch0.add(loop0).extrude(0.04273365722195731)
