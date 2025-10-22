import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.00833).lineTo(0.016, -0.0).lineTo(0.0, -0.00833).lineTo(-0.016, 0.0).lineTo(0.0, 0.00833).close()
solid=wp_sketch0.add(loop0).extrude(-0.001593711955896964)
