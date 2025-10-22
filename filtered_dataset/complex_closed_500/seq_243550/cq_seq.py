import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.32385, -0.37465).lineTo(0.32385, -0.37465).lineTo(0.32385, 0.26035).lineTo(-0.32385, 0.26035).lineTo(-0.32385, -0.37465).close()
solid=wp_sketch0.add(loop0).extrude(0.2600614717980914)
