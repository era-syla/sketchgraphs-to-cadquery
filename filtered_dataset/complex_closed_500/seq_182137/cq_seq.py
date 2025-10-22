import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.06378, 0.0).lineTo(0.06378, -0.01016).lineTo(0.05738, -0.01016).lineTo(0.05738, -0.03048).lineTo(0.06581, -0.03048).lineTo(0.06581, 0.0).lineTo(0.06378, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0031258304615818956)
