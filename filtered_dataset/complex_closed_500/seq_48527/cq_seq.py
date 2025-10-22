import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1604, 0.0004).lineTo(0.1204, 0.0004).lineTo(0.1204, -0.161).lineTo(0.1604, -0.161).lineTo(0.1604, 0.0004).close()
solid=wp_sketch0.add(loop0).extrude(0.432360056875158)
