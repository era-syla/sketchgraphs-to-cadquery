import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0665, -0.0665).lineTo(-0.0665, -0.0665).lineTo(-0.0665, 0.0665).lineTo(0.0665, 0.0665).lineTo(0.0665, -0.0665).close()
solid=wp_sketch0.add(loop0).extrude(0.278295370705197)
