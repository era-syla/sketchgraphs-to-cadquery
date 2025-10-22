import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0127, 0.14288).lineTo(-0.0127, 0.14288).lineTo(-0.0127, -0.14288).lineTo(0.0127, -0.14288).lineTo(0.0127, 0.14288).close()
solid=wp_sketch0.add(loop0).extrude(-0.33404022738397937)
