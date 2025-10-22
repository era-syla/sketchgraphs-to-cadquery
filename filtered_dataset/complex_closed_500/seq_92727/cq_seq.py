import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.59, 0.15).lineTo(0.59, 0.15).threePointArc((0.59707, 0.14707), (0.6, 0.14)).lineTo(0.6, 0.01).threePointArc((0.59707, 0.00293), (0.59, 0.0)).lineTo(-0.59, -0.0).threePointArc((-0.59707, 0.00293), (-0.6, 0.01)).lineTo(-0.6, 0.14).threePointArc((-0.59707, 0.14707), (-0.59, 0.15)).close()
solid=wp_sketch0.add(loop0).extrude(2.4155165665336646)
