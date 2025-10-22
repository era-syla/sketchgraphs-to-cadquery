import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12764, -0.03011).lineTo(-0.08954, -0.03011).lineTo(-0.08954, -0.10631).lineTo(-0.12764, -0.10631).lineTo(-0.12764, -0.03011).close()
solid=wp_sketch0.add(loop0).extrude(-0.14141144763983485)
