import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.10485, -0.17415).lineTo(1.20078, -0.50867).lineTo(1.17579, -0.49482).lineTo(1.091, -0.19913).lineTo(1.10485, -0.17415).close()
solid=wp_sketch0.add(loop0).extrude(0.16714707969501444)
