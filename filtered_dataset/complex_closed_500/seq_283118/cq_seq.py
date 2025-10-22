import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.10795, 0.04484).lineTo(0.1269, 0.04484).lineTo(0.1269, -0.04484).lineTo(0.10795, -0.04484).lineTo(0.10795, 0.04484).close()
solid=wp_sketch0.add(loop0).extrude(0.1836676942853017)
