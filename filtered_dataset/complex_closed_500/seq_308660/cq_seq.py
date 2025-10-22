import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02077, 0.01953).lineTo(-0.31427, 0.01953).lineTo(-0.31427, -0.01684).lineTo(-0.02077, -0.01684).lineTo(-0.02077, 0.01953).close()
solid=wp_sketch0.add(loop0).extrude(0.6218638215186887)
