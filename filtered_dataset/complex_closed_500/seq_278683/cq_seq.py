import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.524, 0.0).lineTo(1.524, 0.0).lineTo(1.524, 2.54).lineTo(-1.524, 3.048).lineTo(-1.524, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-2.0618553681844145)
