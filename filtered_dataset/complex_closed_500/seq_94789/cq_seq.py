import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.09684, 0.06345).lineTo(0.07144, 0.06345).lineTo(0.07144, 0.05869).lineTo(0.09684, 0.05869).lineTo(0.09684, 0.06345).close()
solid=wp_sketch0.add(loop0).extrude(-0.011109082470742616)
