import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.014).lineTo(0.012, 0.014).lineTo(0.021, 0.00679).lineTo(0.021, -0.01021).lineTo(0.0, -0.01021).lineTo(-0.021, -0.01021).lineTo(-0.021, 0.00679).lineTo(-0.012, 0.014).lineTo(0.0, 0.014).close()
solid=wp_sketch0.add(loop0).extrude(-0.08399230675568091)
