import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0785, 0.0385).lineTo(0.0485, 0.0385).lineTo(0.0485, 0.0215).lineTo(0.0785, 0.0215).lineTo(0.0785, 0.0385).close()
solid=wp_sketch0.add(loop0).extrude(-0.045992086694281314)
