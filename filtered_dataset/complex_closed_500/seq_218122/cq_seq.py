import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0165, -0.05592).lineTo(-0.0165, -0.05592).lineTo(-0.0165, -0.03018).lineTo(0.0165, -0.03018).lineTo(0.0165, -0.05592).close()
solid=wp_sketch0.add(loop0).extrude(-0.04227134047540158)
