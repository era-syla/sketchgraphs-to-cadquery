import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0016, 0.0016).lineTo(-0.0016, 0.0016).lineTo(-0.0016, -0.0016).lineTo(0.0016, -0.0016).lineTo(0.0016, 0.0016).close()
solid=wp_sketch0.add(loop0).extrude(-0.005992300318687801)
